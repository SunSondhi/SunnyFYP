module ParticleCloudModule {
    struct Pose {
        double positionx;
        double positiony;
        double positionz;
        double orientationx;
        double orientationy;
        double orientationz;
        double orientationw;
    };

    struct Time {
        long secs;
        long nsecs;
    };


    struct Header {
        long seq;
        Time stamp;
        string frameid;
    };

    sequence<Pose> Poses;

    struct ParticleCloudData {
        Header header;
        Poses poses;
    };

    interface ParticleCloud {
        void receiveParticleCloudData(ParticleCloudData data);
        ParticleCloudData getParticleCloudData();
    };
};
