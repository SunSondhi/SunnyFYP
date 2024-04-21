module TFModule {

    struct Vector3 {
        float x;
        float y;
        float z;
    }

    struct Quaternion {
        float x;
        float y;
        float z;
        float w;
    }

    struct TimeStamp {
        long sec;
        long nanosec;
    }

    struct TFDataStruct {
        TimeStamp header;
        string frameid;
        string childframeid;
        Vector3 translation;
        Quaternion rotation;
        TimeStamp timestamp;
    }

    interface TFData {
        TFDataStruct getTFData();
    };

    interface TransformSender {
        void sendTransformData(TFDataStruct data);
    }

    interface TransformReceiver {
        void receiveTransformData(TFDataStruct data);
    }
}
