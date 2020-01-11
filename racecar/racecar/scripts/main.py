#!/usr/bin/env python
#123
import main2_md

if __name__ == '__main__':
    config = open("/home/nvidia/xycar/src/racecar/racecar/scripts/go2.cfg","r")
    main2_md.main(config)
    config.close()

