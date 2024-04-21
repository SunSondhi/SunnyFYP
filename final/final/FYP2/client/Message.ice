module Message{


     struct TwistData {
        // Define the fields of your message
        double linearx;
        double lineary;
        double linearz;
        double angularx;
        double angulary;
        double angularz;
    }

    interface MessageSender {
        void sendMessage(TwistData data);
    }

}
