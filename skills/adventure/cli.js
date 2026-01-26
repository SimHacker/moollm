#!/usr/bin/env node
/**
 * cli.js — Adventure 4 CLI Runner
 * 
 * Run the adventure engine from the command line.
 * 
 * Usage:
 *   node cli.js                              # Interactive mode
 *   node cli.js world.json                   # Interactive with custom world
 *   node cli.js -e "look" "wallet" "help"    # Execute commands (walkthrough)
 *   node cli.js --exec "go north" "look"     # Same as -e
 *   node cli.js -e "look;wallet;help"        # Semicolon-separated
 */

const fs = require('fs');
const readline = require('readline');

// Parse arguments
const args = process.argv.slice(2);
let worldPath = __dirname + '/dist/world.json';
let commands = [];
let execMode = false;

for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    
    if (arg === '-e' || arg === '--exec') {
        execMode = true;
        // Collect remaining args as commands
        commands = args.slice(i + 1);
        break;
    } else if (arg.endsWith('.json')) {
        worldPath = arg;
    }
}

// Expand semicolon-separated commands
if (commands.length > 0) {
    commands = commands.flatMap(cmd => cmd.split(';').map(c => c.trim()).filter(c => c));
}

// Load engine
const { MootalEngine } = require('./engine.js');

// Load world data
if (!fs.existsSync(worldPath)) {
    console.error(`Error: World file not found: ${worldPath}`);
    console.error('Run the compiler first:');
    console.error('  python3 compile.py ../../examples/adventure-4 --output dist/world.json');
    process.exit(1);
}

const worldData = JSON.parse(fs.readFileSync(worldPath, 'utf8'));

// Create engine
const engine = new MootalEngine();
engine.load(worldData);
engine.setPlayer('character/real-people/don-hopkins');

// Print welcome
console.log(`
╔═══════════════════════════════════════════════════════════════════════════════╗
║  Adventure 4 — CLI Mode                                                       ║
║  "Sheepy enough, but not too sheepy."                                         ║
╚═══════════════════════════════════════════════════════════════════════════════╝

Playing as: ${engine.player.name}
Tags: [${engine.player.tags.join(', ')}]
`);

// Show starting room
console.log(engine.look());
console.log('');

// EXEC MODE: Run commands and exit
if (execMode && commands.length > 0) {
    console.log('─'.repeat(79));
    console.log('WALKTHROUGH MODE');
    console.log('─'.repeat(79));
    console.log('');
    
    for (const cmd of commands) {
        // Echo command
        console.log(`> ${cmd}`);
        console.log('');
        
        // Quit command
        if (['quit', 'exit', 'q'].includes(cmd.toLowerCase())) {
            console.log('Farewell, traveler. The pub will miss you.');
            break;
        }
        
        // Process command
        const result = engine.command(cmd);
        console.log(result);
        console.log('');
    }
    
    console.log('─'.repeat(79));
    console.log('END WALKTHROUGH');
    console.log('─'.repeat(79));
    process.exit(0);
}

// INTERACTIVE MODE: Read from stdin
console.log('Type HELP for commands, QUIT to exit.');
console.log('');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: '> '
});

rl.prompt();

rl.on('line', (line) => {
    const input = line.trim();
    
    // Echo command (helps when piping input)
    console.log(input);
    
    if (!input) {
        rl.prompt();
        return;
    }
    
    // Quit command
    if (['quit', 'exit', 'q'].includes(input.toLowerCase())) {
        console.log('\nFarewell, traveler. The pub will miss you.\n');
        rl.close();
        process.exit(0);
    }
    
    // Process command
    const result = engine.command(input);
    console.log('');
    console.log(result);
    console.log('');
    
    rl.prompt();
});

rl.on('close', () => {
    process.exit(0);
});
