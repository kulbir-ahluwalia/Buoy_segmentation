# Output video
Link: https://drive.google.com/drive/u/2/folders/1gdFTJFqFFvxLCYgYxuwSgpzTNCbogE3c 

# Buoy_segmentation for 3D gaussian
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


# Buoy_segmentation for 1D gaussian
To detect the yellow buoy, open a terminal and run:-
``` 
python3 generate1DBinaryVideo_yellow.py
```

To detect the orange buoy, open a terminal and run:- 
```
python3 generate1DBinaryVideo_orange.py
```

To detect the green buoy, open a terminal and run:-
```
python3 generate1DBinaryVideo_green.py
```


## Dataset generation
To extract the RGB values corresponding to pixels of a particular colour:-
```
cd Code/Dataset_generation
python3 extract_pixel_values.py
```
It will generate csv files named yellow_buoy_dataset.csv, orange_buoy_dataset.csv and green_buoy_dataset.csv.
