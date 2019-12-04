LANDRS_Babelfish directory structure currently:

├── autopilot_interface.cpp     //Borrowed from Mavlink UART eg
├── autopilot_interface.h       // As above
├── cmake-build-debug           // Build directory
├── CMakeLists.txt
├── docs                        //Empty for now but will contain doxygen config and outputs
├── example_data
├── geomavlink.cpp              // Demo application source
├── geomavlink.h                // Demo application header
├── LANDRSbabelfish             // library we want to develop and used in demo application
├── LICENSE
├── README.md                   // See build instructions here, should work exactly the same as c_uart example
├── serial_port.cpp             // Serial interface copied from c_uart eg
├── serial_port.h               // as above
├── tests                       // Currently empty - I'll get there this weekend, doesn't matter now
└── third_party                 // External libraries we're pulling in including main mavlink and json lib 

Next steps:
1. Clone and get it to build (see README or if you're using CLion/another IDE that knows how to use cmake should build it for you with the IDE biuld command)

2. Check it works the same as the c_uart example did
(BTW, I found my autopilot at least responded quicker when I flashed it with Px4.  not sure if that will be the same for you or not but give it a try if it's being slow.  If MissionPlanner is crashing on you, try QGroundControl for flashing the FW

3. Once above works:  
- If you open the geomavlink.h and cpp  
To keep it simple for now I've left everything as is, all I've changes is I've added a new geomav_commands() function that I want to call instead of the current commands() function.  We need to flesh that out.  Read through the whole file but also ctrl-F for "TODO" to jump straight to the edited portions

- If you look inside LANDRSBabelfish you'll find converter_I.h 
This is the file we need to build, it will define the library interface: so functions that can convert any and every mavlink msg into <specified file format>.   The goal being so we can have a single set of functions that can take in all possible mavlink messages and then in multiple different instantiation classes depending on the format requested, the functions can be implemented differently to output different formts.

This looks like a reasonable json lib but I haven't added it to the cmake yet
https://github.com/nlohmann/json
