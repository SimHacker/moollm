# Data source tracking for --sources (LLM self-service).

from typing import Dict, Set

SOURCES_MODE = False
_data_sources: Dict[str, Set[str]] = {
    "databases": set(),
    "tables": set(),
    "files": set(),
    "directories": set(),
    "sql_queries": set(),
}

def set_sources_mode(enabled: bool) -> None:
    """Enable data source tracking for LLM self-service."""
    global SOURCES_MODE
    SOURCES_MODE = enabled

def register_source(source_type: str, path_or_query: str, table: str = None) -> None:
    """Register a data source for later reporting."""
    if not SOURCES_MODE:
        return
    if source_type == "database":
        _data_sources["databases"].add(str(path_or_query))
        if table:
            _data_sources["tables"].add(table)
    elif source_type == "file":
        _data_sources["files"].add(str(path_or_query))
    elif source_type == "directory":
        _data_sources["directories"].add(str(path_or_query))
    elif source_type == "sql":
        query = str(path_or_query).strip()[:200]
        _data_sources["sql_queries"].add(query)

def print_sources() -> None:
    """Print all registered data sources for LLM self-service."""
    print("\nDATA SOURCES -- Query these directly for raw access")

    if _data_sources["databases"]:
        print("\n📁 DATABASES (SQLite - use: sqlite3 <path>):")
        for db in sorted(_data_sources["databases"]):
            print(f"   {db}")

    if _data_sources["tables"]:
        print("\n📊 TABLES queried:")
        for t in sorted(_data_sources["tables"]):
            print(f"   {t}")

    if _data_sources["sql_queries"]:
        print("\n🔍 SQL QUERIES used (adapt for your needs):")
        for q in list(_data_sources["sql_queries"])[:10]:
            print(f"   {q}...")

    if _data_sources["files"]:
        print("\n📄 FILES read:")
        for f in sorted(_data_sources["files"]):
            print(f"   {f}")

    if _data_sources["directories"]:
        print("\n📂 DIRECTORIES scanned:")
        for d in sorted(_data_sources["directories"]):
            print(f"   {d}")

    print("\nTIP: Use 'sqlite3 <db_path> \".tables\"' to list all tables")
    print("TIP: Use 'sqlite3 <db_path> \".schema <table>\"' to see schema")
    print("TIP: Use 'sqlite3 <db_path> \"SELECT * FROM <table> LIMIT 5\"' to sample data")
