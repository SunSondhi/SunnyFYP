module LaserModule {
	
    sequence<float> Floats;

    struct LaserScan {
        
        int seq;
        int sec;
        int nsec;
        string frameId;
        float angleMin;
        float angleMax;
        float angleIncrement;
        float timeIncrement;
        float scanTime;
        float rangeMin;
        float rangeMax;
        Floats ranges;
        Floats intensities;
    };

    interface LaserData {
        void publishLaserScan(LaserScan scan);
        LaserScan getLatestLaserData();
    };
};

