Flashing Procedure
Seagate v0.4.1

1. Flash bootloader
    python esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 921600 --before default_reset --after no_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x1000 bootloader.bin

2. Flash application, partition table, and ota initial data
    python esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 921600 --before default_reset --after hard_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0xd000 ota_data_initial.bin 0x10000 oralb_turing_seagate.bin 0xa000 my_partitions.bin

With device powered, wait approximately 10 - 20 seconds for bootloader to encrypt partitions and reboot. You should see the device go through LED bootup sequence (RED->GREEN->BLUE->WHITE). At this point, the device should be ready to test and use.
