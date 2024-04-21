module MapModule {
    struct Time {
        long secs;
        long nsecs;
    };

    struct Pose {
        double positionx;
        double positiony;
        double positionz;
        double orientationx;
        double orientationy;
        double orientationz;
        double orientationw;
    };


    struct Header {
        long seq;
        Time stamp;
        string frameid;  
    };

    struct MapMetaData {
        Time maploadtime;
        double resolution;
        long width;
        long height;
        Pose origin;
    };

    sequence<long> data;

    struct OccupancyGridData {
        long seqnum;
        data data;
    };


    struct MapInfo {
        Header header;
        Time timestamp;
        MapMetaData metadata;
        OccupancyGridData griddata;
    };

    interface MapData {
        MapInfo getLatestMapData();
    };
};
