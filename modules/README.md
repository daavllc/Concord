# Concord Modules
Modules can be created, configured, and loaded to preform specific tasks

# Structure
Note: Additional files may be included, but must be referenced within the module's "init.py" in order to do anything.
- conf.py: Contains module-specific configuration information used directly within the code. If the module contains a serialized configuration, it should be assumed that "conf.py" can be updated as Concord updates, while the serialized confguration is not.
- init.py: init() is called when the module is loaded