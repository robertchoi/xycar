#!/usr/bin/env python
#123
import test_xytron_md

if __name__ == '__main__':
    config = open("/home/nvidia/xycar/src/racecar/racecar/scripts/go4.cfg","r")
    test_xytron_md.main(config)
    config.close()
