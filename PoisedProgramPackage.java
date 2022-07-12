public class PoisedProgramPackage {

    //Attributes
    int projectNumber;
    String projectName;
    String buildingType;
    String projectAddress;
    String erfNumber;
    double totalFeeCharge;
    double amountPaid;
    String deadLine;


    //constructor created to display the project details.
    public PoisedProgramPackage(int projectNumber, String projectName, String buildingType, String projectAddress,
                                String erfNumber, double totalFeeCharge, double amountPaid, String deadLine){

        //referencing the parameters in
        //the constructor created above.
        this.projectNumber = projectNumber;
        this.projectName = projectName;
        this.buildingType = buildingType;
        this.projectAddress = projectAddress;
        this.erfNumber = erfNumber;
        this.totalFeeCharge = totalFeeCharge;
        this.amountPaid = amountPaid;
        this.deadLine = deadLine;

    }

    //toString method created to display the
    //project state in the Poised.java mainprogram.
    public String toString ()
    {
        String output = "Project Number:" +projectNumber;
        output += "\nProject Name:" +projectName;
        output += "\nBuilding Type:" + buildingType;
        output += "\nProject Address:" + projectAddress;
        output += "\nERF Number:" + erfNumber;
        output += "\nTotal Fee Charged:" + totalFeeCharge;
        output += "\nAmount Paid:" + amountPaid;
        output += "\nDeadline:" + deadLine;

        return output;

    }

}
