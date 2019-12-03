# LANDRS_Babelfish

A python module for converting Mavlink2[](https://github.com/mavlink/c_library_v2) messages and flightlogs into [GeojsonLD](http://geojson.org/geojson-ld/).  

## Caveats while in beta
- Initially this code converts to GEOJSON, LD functionality is the first second version priority
- Ardupilot interoperability is equally a priority, however, an unknown bug means initial code has only been tested and verified with Px4
- An end goal is for this to be deplyable via: docker container, systemd service, and as a  cpp library with automated CI.  However for initial release it will be deployed as an example application

## Contributing
**This project is only begining 18 November 2019** but is and always will be published openly under Apache 2.0.  PRs and issue submissions are welcomed.

## About the LANDRS project under which this module is being developed
This is a project under development by the Sloan Foundation supported Linked And Networked DRoneS (LANDRS) project which is working to build foundational infrastructure for the support of Unmanned Vehicles.  Specifically this project is aimed at building ontologies and supporting code APIs to facilitate communities building applications that leverage the power of linked data and the semantic web to facilitate researchers capturing and publishing Findable Accessible Interoperable and Reusable data using UxVs (colloquially known as 'drones').  While focuses on small scale unmanned aerial vehicles the project intends to build infrastructure that is both scientific and usecase domain agnostic and which might serve a range of unmanned vehicles potentially including ground rovers, and watercraft.

# Building
Assumes a \*nix system

```
$ cd LANDRS_Babelfish/
$ git submodule update --init --recursive
$ mkdir build
$ cd build
$ cmake ../
$ cmake --build . --target all -- -j 2
$ ./GeoMav -d /dev/<Path to mavlink port>  #Eg: /dev/ttyACM0
```
