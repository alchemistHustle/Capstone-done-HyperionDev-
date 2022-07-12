public class PoisedObjects {

    //Attributes
    String title;
    String name;
    String telephoneNum;
    String emailAddress;
    String physicalAddress;

    //Methods
    public PoisedObjects (String title, String name, String telephoneNum, String emailAddress, String physicalAddress)
    {
        this.title = title;
        this.name = name;
        this.telephoneNum = telephoneNum;
        this.emailAddress = emailAddress;
        this.physicalAddress = physicalAddress;
    }


    //toString Method
    public String toString()
    {
        String output = "Title:" + title;
        output += "\nName:" + name;
        output += "\nTelephone Number:" + telephoneNum;
        output += "\nEmail Address:" + emailAddress;
        output += "\nPhysical Address:" + physicalAddress;

        return output;
    }


}
