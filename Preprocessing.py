import splitfolders
input_folder="G:\CAP 6545\ClassGastric-main\GasHisSDB/160"
output_folder="G:\CAP 6545\ClassGastric-main\Dataset"
splitfolders.ratio(input_folder,output=output_folder,ratio=(.7,.2,.1),seed=38)
