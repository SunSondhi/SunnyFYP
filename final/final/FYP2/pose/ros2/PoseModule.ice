module PoseModule {
    interface PoseData {
        void publishPoseData(string data);
        string getLatestPoseData();
    };
};
