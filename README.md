# Buoy_segmentation
To detect the yellow buoy, open a terminal and run: 
``` 
python3 generate_yellow_video.py
```

To detect the orange buoy, open a terminal and run:  
```
python3 generate_orange_video.py
```

To detect the green buoy, open a terminal and run:  
```
python3 generate_green_video.py
```

## Dataset generation
To extract the RGB values corresponding to pixels of a particular colour:
```
cd Code/Dataset_generation
python3 extract_pixel_values.py
```
It will generate csv files named yellow_buoy_dataset.csv, orange_buoy_dataset.csv and green_buoy_dataset.csv.