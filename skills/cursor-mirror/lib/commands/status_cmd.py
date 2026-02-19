# Status commands: status, config, mcp, models, features, privacy, endpoints
# Extracted from cursor_mirror_old.py during Phase 2 refactoring.

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml
import os

from ..db import open_db, decode_blob, get_item_table_value, get_reactive_storage
from ..paths import GLOBAL_DB, WORKSPACES_ROOT, BASE_DIR
from ..keys import SESSION_LIST_KEYS, COMPOSER_STATE_KEY, NOTABLE_GLOBAL_KEYS
from ..discovery import iter_workspace_paths, get_workspace_folder, folder_uri_to_path
from ..composers import get_workspace_composers, get_all_composers, get_bubble_counts, clear_caches
from ..bubbles import iter_bubbles, load_bubbles, get_bubble_text, has_content, extract_bubble_text, is_error, USER, ASSISTANT
from ..resolve import resolve_workspace, resolve_composer, resolve_composer_id
from ..format_util import format_ts, get_output_format, output_data, format_not_supported
from ..debug_util import debug
from ..sources import register_source


def cmd_status(args):
    """Overall Cursor status dashboard."""
    # Count bubbles and composers
    bubble_counts = get_bubble_counts()
    total_msgs = sum(bubble_counts.values())
    num_composers = len(bubble_counts)
    
    # MCP servers
    mcp_servers = get_item_table_value("mcpService.knownServerIds") or []
    
    # Server config
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    
    # Reactive storage for AI settings
    reactive = get_reactive_storage()
    ai_settings = reactive.get("aiSettings", {})
    
    # Feature config
    feature_config = get_item_table_value("cursorai/featureConfigCache") or {}
    feature_status = get_item_table_value("cursorai/featureStatusCache") or {}
    
    # Privacy
    privacy_mode = get_item_table_value("cursorai/donotchange/privacyMode")
    
    status = {
        "cursor_status": {
            "total_composers": num_composers,
            "total_messages": total_msgs,
            "mcp_servers_registered": len(mcp_servers),
            "privacy_mode": privacy_mode,
        },
        "ai_settings": {
            "composer_model": ai_settings.get("composerModel", "default"),
            "chat_model": ai_settings.get("regularChatModel", "default"),
            "model_override_enabled": ai_settings.get("modelOverrideEnabled", False),
        },
        "limits": {
            "context_tokens": server_config.get("chatConfig", {}).get("fullContextTokenLimit", "?"),
            "max_mcp_tools": server_config.get("chatConfig", {}).get("maxMcpTools", "?"),
            "max_files_indexed": server_config.get("indexingConfig", {}).get("absoluteMaxNumberFiles", "?"),
        },
        "features_enabled": sum(1 for v in feature_status.values() if v),
        "features_total": len(feature_status),
    }
    
    out_fmt = get_output_format(args)
    
    if out_fmt != "text":
        output_data(status, out_fmt, "status", 
                   supported=["text", "json", "jsonl", "yaml", "csv", "md"])
    else:
        print("CURSOR STATUS")
        print(f"Composers: {status['cursor_status']['total_composers']}    Messages: {status['cursor_status']['total_messages']}")
        print(f"MCP Servers: {status['cursor_status']['mcp_servers_registered']}    Privacy: {'ON' if privacy_mode else 'OFF'}")
        print("AI Settings")
        print(f"  Composer Model: {status['ai_settings']['composer_model']}")
        print(f"  Chat Model: {status['ai_settings']['chat_model']}")
        print("Limits")
        print(f"  Context Tokens: {status['limits']['context_tokens']}")
        print(f"  Max MCP Tools: {status['limits']['max_mcp_tools']}")
        print(f"  Max Files Index: {status['limits']['max_files_indexed']}")
        print(f"Features: {status['features_enabled']}/{status['features_total']} enabled")
        print("\nRun 'status-config', 'status-mcp', 'status-models' for details.")


def cmd_status_config(args):
    """Server configuration and limits."""
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    
    config = {
        "indexing": server_config.get("indexingConfig", {}),
        "chat": server_config.get("chatConfig", {}),
        "background_composer": server_config.get("backgroundComposerConfig", {}),
        "tracing": server_config.get("clientTracingConfig", {}),
        "bugbot": server_config.get("bugConfigResponse", {}),
        "config_version": server_config.get("configVersion", "unknown"),
    }
    
    if get_output_format(args) != "text":
        print(fmt(config, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    SERVER CONFIGURATION                      ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        idx = config.get("indexing", {})
        print("║  Indexing                                                    ║")
        print(f"║    Max Files:          {idx.get('absoluteMaxNumberFiles', '?'):>10}                      ║")
        print(f"║    Concurrent Uploads: {idx.get('maxConcurrentUploads', '?'):>10}                      ║")
        print(f"║    Sync Concurrency:   {idx.get('syncConcurrency', '?'):>10}                      ║")
        print(f"║    Index Period (sec): {idx.get('indexingPeriodSeconds', '?'):>10}                      ║")
        print(f"║    Max Batch Bytes:    {idx.get('maxBatchBytes', '?'):>10}                      ║")
        
        chat = config.get("chat", {})
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Chat                                                        ║")
        print(f"║    Context Token Limit:   {chat.get('fullContextTokenLimit', '?'):>10}                   ║")
        print(f"║    Max Rule Length:       {chat.get('maxRuleLength', '?'):>10}                   ║")
        print(f"║    Max MCP Tools:         {chat.get('maxMcpTools', '?'):>10}                   ║")
        print(f"║    MCP Tools Warning:     {chat.get('warnMcpTools', '?'):>10}                   ║")
        
        bg = config.get("background_composer", {})
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Background Composer                                         ║")
        print(f"║    Enabled:           {str(bg.get('enableBackgroundAgent', '?')):>10}                      ║")
        print(f"║    Max Windows:       {bg.get('maxWindowInWindows', '?'):>10}                      ║")
        print(f"║    Preload Count:     {bg.get('windowInWindowPreloadCount', '?'):>10}                      ║")
        
        print("╠──────────────────────────────────────────────────────────────╣")
        print(f"║  Config Version: {config.get('config_version', 'unknown')[:40]:40} ║")
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_mcp(args):
    """MCP servers and status."""
    mcp_servers = get_item_table_value("mcpService.knownServerIds") or []
    reactive = get_reactive_storage()
    mcp_config = reactive.get("mcpServers", [])
    
    # Categorize servers
    builtin = [s for s in mcp_servers if s.startswith("cursor-")]
    user = [s for s in mcp_servers if s.startswith("user-")]
    project = [s for s in mcp_servers if s.startswith("project-")]
    other = [s for s in mcp_servers if not any(s.startswith(p) for p in ["cursor-", "user-", "project-"])]
    
    result = {
        "total_servers": len(mcp_servers),
        "builtin": builtin,
        "user_configured": user,
        "project_scoped": project,
        "other": other,
    }
    
    if get_output_format(args) != "text":
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                      MCP SERVERS                             ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Total Registered: {len(mcp_servers):>3}                                       ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        if builtin:
            print("║  Built-in                                                    ║")
            for s in builtin:
                print(f"║    • {s[:54]:54} ║")
        
        if user:
            print("╠──────────────────────────────────────────────────────────────╣")
            print("║  User-Configured                                             ║")
            for s in user:
                display = s.replace("user-", "")
                print(f"║    • {display[:54]:54} ║")
        
        if project:
            print("╠──────────────────────────────────────────────────────────────╣")
            print("║  Project-Scoped                                              ║")
            for s in project[:10]:  # Limit display
                display = s.replace("project-", "")
                print(f"║    • {display[:54]:54} ║")
            if len(project) > 10:
                print(f"║    ... and {len(project) - 10} more                                          ║")
        
        if other:
            print("╠──────────────────────────────────────────────────────────────╣")
            print("║  Other                                                       ║")
            for s in other[:5]:
                print(f"║    • {s[:54]:54} ║")
        
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_models(args):
    """Available models and migrations."""
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    reactive = get_reactive_storage()
    
    available_models = reactive.get("availableDefaultModels2", [])
    ai_settings = reactive.get("aiSettings", {})
    migrations = server_config.get("modelMigrations", [])
    
    # Parse model capabilities
    models_by_capability = {
        "agent": [],
        "thinking": [],
        "images": [],
        "max_mode": [],
        "plan_mode": [],
        "sandboxing": [],
    }
    
    for m in available_models:
        name = m.get("model", m.get("name", "unknown"))
        if m.get("supportsAgent"):
            models_by_capability["agent"].append(name)
        if m.get("supportsThinking"):
            models_by_capability["thinking"].append(name)
        if m.get("supportsImages"):
            models_by_capability["images"].append(name)
        if m.get("supportsMaxMode"):
            models_by_capability["max_mode"].append(name)
        if m.get("supportsPlanMode"):
            models_by_capability["plan_mode"].append(name)
        if m.get("supportsSandboxing"):
            models_by_capability["sandboxing"].append(name)
    
    result = {
        "total_models": len(available_models),
        "current_settings": {
            "composer": ai_settings.get("composerModel", "default"),
            "chat": ai_settings.get("regularChatModel", "default"),
            "openai": ai_settings.get("openAIModel", "default"),
        },
        "models_by_capability": {k: len(v) for k, v in models_by_capability.items()},
        "recent_migrations": [{
            "from": m.get("previousModel"),
            "to": m.get("targetModel"),
            "setting": m.get("modelSetting"),
        } for m in migrations[:5]],
        "all_models": [m.get("model", m.get("name", "?")) for m in available_models],
    }
    
    if get_output_format(args) != "text":
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                      AI MODELS                               ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Total Available: {len(available_models):>3}                                        ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  Current Settings                                            ║")
        print(f"║    Composer: {str(result['current_settings']['composer'])[:45]:45} ║")
        print(f"║    Chat:     {str(result['current_settings']['chat'])[:45]:45} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Capabilities (model count)                                  ║")
        print(f"║    Agent: {len(models_by_capability['agent']):>3}  Thinking: {len(models_by_capability['thinking']):>3}  Images: {len(models_by_capability['images']):>3}  Max: {len(models_by_capability['max_mode']):>3}  ║")
        print(f"║    Plan: {len(models_by_capability['plan_mode']):>3}   Sandbox: {len(models_by_capability['sandboxing']):>3}                                  ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Recent Migrations                                           ║")
        for m in migrations[:3]:
            fr = m.get("previousModel", "?")[:20]
            to = m.get("targetModel", "?")[:20]
            print(f"║    {fr:20} → {to:20}         ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  All Models                                                  ║")
        model_names = [m.get("model", m.get("name", "?")) for m in available_models]
        # Print 2 per line
        for i in range(0, min(len(model_names), 20), 2):
            m1 = model_names[i][:28]
            m2 = model_names[i+1][:28] if i+1 < len(model_names) else ""
            print(f"║    {m1:28} {m2:28} ║")
        if len(model_names) > 20:
            print(f"║    ... and {len(model_names) - 20} more                                        ║")
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_features(args):
    """Feature flags and experiments."""
    feature_status = get_item_table_value("cursorai/featureStatusCache") or {}
    feature_config = get_item_table_value("cursorai/featureConfigCache") or {}
    reactive = get_reactive_storage()
    
    # Group features
    enabled = {k: v for k, v in feature_status.items() if v}
    disabled = {k: v for k, v in feature_status.items() if not v}
    
    # Interesting reactive toggles
    toggles = {
        "yoloMode": reactive.get("composerState", {}).get("yoloModeEnabled"),
        "isLinterEnabled": reactive.get("isLinterEnabled"),
        "autopilotEnabled": reactive.get("autopilotFeatureEnabled"),
        "bugbotEnabled": reactive.get("bugbotState", {}).get("isEnabled"),
        "semanticSearch": reactive.get("explicitlyEnableSemanticSearch"),
        "memoriesEnabled": reactive.get("cursor/memoriesEnabled"),
    }
    
    result = {
        "feature_flags": {
            "enabled_count": len(enabled),
            "disabled_count": len(disabled),
            "enabled_list": list(enabled.keys()),
        },
        "feature_config": feature_config,
        "reactive_toggles": toggles,
    }
    
    if get_output_format(args) != "text":
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    FEATURE FLAGS                             ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║  Enabled: {len(enabled):>3}    Disabled: {len(disabled):>3}                             ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  Reactive Toggles                                            ║")
        for name, val in toggles.items():
            status = "✓" if val else "✗" if val is False else "?"
            print(f"║    [{status}] {name:52} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Enabled Feature Flags                                       ║")
        for f in list(enabled.keys())[:15]:
            print(f"║    • {f[:54]:54} ║")
        if len(enabled) > 15:
            print(f"║    ... and {len(enabled) - 15} more                                          ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Feature Config (Limits)                                     ║")
        for k, v in list(feature_config.items())[:10]:
            print(f"║    {k[:30]:30} = {str(v)[:20]:20} ║")
        print("╚══════════════════════════════════════════════════════════════╝")


def cmd_status_privacy(args):
    """Privacy settings and data sharing."""
    privacy_mode = get_item_table_value("cursorai/donotchange/privacyMode")
    new_privacy = get_item_table_value("newPrivacyMode2")
    partner_share = get_item_table_value("partnerDataShare")
    
    reactive = get_reactive_storage()
    memories_enabled = reactive.get("cursor/memoriesEnabled")
    pending_memories = get_item_table_value("cursorPendingMemories") or []
    
    # Tracing config
    server_config = get_item_table_value("cursorai/serverConfig") or {}
    tracing = server_config.get("clientTracingConfig", {})
    metrics = server_config.get("metricsConfig", {})
    
    result = {
        "privacy_mode": privacy_mode,
        "new_privacy_mode": new_privacy,
        "partner_data_share": partner_share,
        "memories": {
            "enabled": memories_enabled,
            "pending_count": len(pending_memories),
        },
        "telemetry": {
            "traces_sample_rate": tracing.get("tracesSampleRate"),
            "logger_sample_rate": tracing.get("loggerSampleRate"),
            "error_rate_limit": tracing.get("errorRateLimit"),
            "metrics_in_privacy_mode": metrics.get("enabledInPrivacyMode"),
        },
    }
    
    if get_output_format(args) != "text":
        print(fmt(result, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    PRIVACY SETTINGS                          ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        pm_status = "ENABLED" if privacy_mode else "DISABLED"
        print(f"║  Privacy Mode: {pm_status:>10}                                  ║")
        print(f"║  Partner Data Share: {str(partner_share):>10}                          ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Memories                                                    ║")
        mem_status = "✓ Enabled" if memories_enabled else "✗ Disabled"
        print(f"║    Status: {mem_status:20}                          ║")
        print(f"║    Pending: {len(pending_memories):>5} memories waiting to sync                ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Telemetry Sampling                                          ║")
        print(f"║    Traces:  {tracing.get('tracesSampleRate', '?'):>10}                                 ║")
        print(f"║    Logger:  {tracing.get('loggerSampleRate', '?'):>10}                                 ║")
        print(f"║    Metrics in privacy mode: {str(metrics.get('enabledInPrivacyMode', '?')):>10}              ║")
        print("╚══════════════════════════════════════════════════════════════╝")


# SQL & database commands


def cmd_status_endpoints(args):
    """Known API endpoints."""
    endpoints = {
        "ai_backends": {
            "primary": "agent.api5.cursor.sh",
            "fallbacks": ["api2.cursor.sh", "api3.cursor.sh", "api4.cursor.sh"],
            "geo_optimized": {
                "us_west": "agent-gcpp-uswest.api5.cursor.sh",
                "eu_central": "agent-gcpp-eucentral.api5.cursor.sh",
            },
        },
        "semantic_search": {
            "primary": "repo42.cursor.sh",
            "purpose": "Codebase embedding and retrieval",
        },
        "telemetry": {
            "metrics": "metrics.cursor.sh",
            "purpose": "Error and performance tracking",
        },
        "marketplace": {
            "primary": "marketplace.cursorapi.com",
            "alternate": "marketplace.cursor.sh",
        },
        "updates": {
            "changelog": "changelog.cursor.com",
            "staging": "dev-staging.cursor.sh",
        },
        "internal": {
            "replay": "anytool.corp.anysphere.co/api/replay-chat",
            "docs": "docs.anysphere.dev",
        },
    }
    
    if get_output_format(args) != "text":
        print(fmt(endpoints, args))
    else:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    API ENDPOINTS                             ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║  AI Backends                                                 ║")
        print(f"║    Primary:    {endpoints['ai_backends']['primary']:44} ║")
        print(f"║    US West:    {endpoints['ai_backends']['geo_optimized']['us_west']:44} ║")
        print(f"║    EU Central: {endpoints['ai_backends']['geo_optimized']['eu_central']:44} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Semantic Search                                             ║")
        print(f"║    {endpoints['semantic_search']['primary']:56} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Telemetry                                                   ║")
        print(f"║    {endpoints['telemetry']['metrics']:56} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Marketplace                                                 ║")
        print(f"║    {endpoints['marketplace']['primary']:56} ║")
        print("╠──────────────────────────────────────────────────────────────╣")
        print("║  Internal (Debug)                                            ║")
        print(f"║    {endpoints['internal']['replay']:56} ║")
        print("╚══════════════════════════════════════════════════════════════╝")

