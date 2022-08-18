
# out_main <- "/home/satyukt/Projects/1000/crop_health_report/phi_out/"

long2UTM <- function(long) {
  (floor((long + 180)/6) %% 60) + 1
}

area_function <- function(farm_id){  
    area_files<-Sys.glob(paste0(area_folder_path,farm_id,".csv"))
    filename<-tools::file_path_sans_ext(basename(area_files))
    wkt <- read.table(area_files,header = FALSE, sep = "\t",stringsAsFactors = FALSE)
    shp_poly <- readWKT(wkt$V1)
    crs(shp_poly) <- "+proj=longlat +datum=WGS84 +no_defs"
    shp_file_st <-st_as_sfc(shp_poly)
    utmzone=32600+long2UTM(st_bbox(shp_file_st)$xmin)
    shp_file_st <- st_transform(shp_file_st,utmzone)
    area =st_area(shp_file_st)
    area_ha = as.numeric(area/10000)
    
    # if(area_ha <1){
    #   zones=1
    # }
    # else if(area_ha >1 & area_ha <10){
    #   zones=2
    # }
    # else if(area_ha >10){
    #   zones=3
    # }
    return(area_ha)

    }
# area_function(10000)
