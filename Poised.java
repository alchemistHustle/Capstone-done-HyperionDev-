/*This is the Poised Main program
it consists of the Menu that calls the method from the other two classes
'PoisedProgramPackage' and 'PoisedObjects'.
The program will require the user to capture new project.
The information entered by the user will be built into an object
and displayed to the user.
 */

//Scanner module to input.
import java.util.Scanner;

public class Poised { //Main class for the Poised program.

    public static void main(String[] args) //Main Method for the program.
    {

        //Variables to be used in the program.
        int projectNumber;
        String projectName;
        String buildingType;
        String projectAddress;
        String erfNumber;
        double totalFeeCharge;
        double amountPaid;
        String deadLine;

        //Declared Variable for individual type.
        //to be used later on.
        String title = "contractor";

        //Welcome message to the user.
        System.out.println("Welcome to Poised Management System. You can go ahead and create a new project!");

        //user will be prompted to enter details for the project.
        //the data will be stored in the appropriate variables.
        //project number to be entered here.
        System.out.println("\nEnter a new project number: ");
        Scanner userInput1 = new Scanner (System.in);
        projectNumber = userInput1.nextInt();

        //project name to be entered here.
        System.out.println("\nEnter a project name: ");
        Scanner userInput2 = new Scanner (System.in);
        projectName = userInput2.nextLine();

        //building type to be entered here.
        System.out.println("\nEnter building type: ");
        Scanner userInput3 = new Scanner(System.in);
        buildingType = userInput3.nextLine();

        //project address to be entered here.
        System.out.println("\nEnter project address: ");
        Scanner userInput4 = new Scanner(System.in);
        projectAddress = userInput4.nextLine();

        //ERF number to be entered here.
        System.out.println("\nEnter ERF number: ");
        Scanner userInput5 = new Scanner(System.in);
        erfNumber = userInput5.nextLine();

        //total fee charged for project to be entered here.
        System.out.println("\nEnter the total fee charged for the project: ");
        Scanner userInput6 = new Scanner(System.in);
        totalFeeCharge = userInput6.nextDouble();

        //amount paid by client to be entered here.
        System.out.println("\nEnter total amount paid till date: ");
        Scanner userInput7 = new Scanner(System.in);
        amountPaid = userInput7.nextDouble();

        //project deadline to be entered here.
        System.out.println("\nEnter project deadline - DD/MM/YYYY: ");
        Scanner userInput8 = new Scanner(System.in);
        deadLine = userInput8.nextLine();

        //a new project is then created using the details entered by the user above
        // using the PoisedProgramPackage class method that was created in a separate file.
        PoisedProgramPackage newProjectCaptured = new PoisedProgramPackage(projectNumber, projectName, buildingType,
                projectAddress, erfNumber, totalFeeCharge, amountPaid, deadLine);

        //the ToString Method created in PoisedProgramPackage will be called
        //to display the details entered by the user.
        System.out.println(newProjectCaptured.toString());


        //this will be displayed to the user after the details for the project has been entered.
        System.out.println("\nProject Successfully Created!.");

        //User will be displayed the below menu if they wish to 'edit', 'update', and finalise the project
        //or exit the program.
        System.out.println("\nPlease choose a number option from the menu below: \n"+ "\n1. Edit existing projects"
        +"\n2. Update contractor details" + "\n3. Finalise the project" + "\n4. Exit program");

        //getting user input choice and storing it in 'userChoice' variable.
        Scanner userInput = new Scanner(System.in);
        int userChoice = userInput.nextInt();

        //conditional statement if userChoice is 1.
        if (userChoice == 1)
        {
            //User is then given two options to edit the project or edit total amount paid.
            System.out.println("\nWould you like to:" + "\n1.Edit project due date: "+ "\n2.Edit total amount paid till" +
                    " date: ");

            //scanner module to collect input from user.
            //data collected from user will be stored in the 'editChoice' variable.
            Scanner choice = new Scanner(System.in);
            int editChoice = choice.nextInt();

            //conditional statement of user chooses 1.
            if (editChoice == 1)

            {
                //if user chooses one they are required to enter a due date.
                System.out.println("Enter new due date of project - DD/MM/YYYY: ");
                Scanner date = new Scanner(System.in);

                //deadline variable to store the input from user.
                deadLine = date.nextLine();

                //projectEdit object to include the new date entered by user.
                PoisedProgramPackage projectEdit = new PoisedProgramPackage(projectNumber,projectName,buildingType,
                        projectAddress,erfNumber,totalFeeCharge,amountPaid,deadLine);
                System.out.println(projectEdit.toString()); //we call the toString method to display data entered by
                                                            //user.

            }
            //if user choose 2
            else if (editChoice == 2)
            {
                //user is asked to enter an amount paid till date.
                System.out.println("\nEnter a new total amount paid till date: ");
                Scanner amount = new Scanner(System.in);

                //we store the input in the 'amountPaid' variable.
                amountPaid = amount.nextLong();

                PoisedProgramPackage projectEdit2 = new PoisedProgramPackage(projectNumber,projectName,buildingType,
                        projectAddress,erfNumber,totalFeeCharge,amountPaid,deadLine);
                System.out.println(projectEdit2.toString()); //we display the edited information using the
                                                            //ToString method created in our 'PoisedProgramPackage'
                                                            //class.
            }




        }
        //conditional statement if userChoice is 2.
        else if (userChoice == 2)
        {
            //user will be prompted to enter the contractor's name
            //to confirm their details.
            System.out.println("\nEnter the contractor's name to confirm their details: ");
            Scanner nameEdit = new Scanner(System.in);
            String name = nameEdit.nextLine();

            //user will be prompted to enter contractor's new
            //contact and stored in the newNumber variable.
            System.out.println("\nPlease enter the new contractor's new contact number: ");
            Scanner newNumber = new Scanner (System.in);
            String telephoneNum = newNumber.nextLine();

            //user will be prompted to enter contractor's new
            //email address and stored in the newEmail variable.
            System.out.println("Enter the new contractor's email address: ");
            Scanner newEmail = new Scanner (System.in);
            String emailAddress = newEmail.nextLine();

            //user will be prompted to enter contractor's new
            //physical address and stored in the newAddress variable.
            System.out.println("Enter contractor's new physical address: ");
            Scanner newAddress = new Scanner (System.in);
            String physicalAddress = newAddress.nextLine();


            //information entered for the new contractor
            //will be used to create a new object.
            PoisedObjects contractorEdit = new PoisedObjects(title,name,telephoneNum,emailAddress,physicalAddress);


            //we display the new details using the toString method
            //created in the PoisedObjects class.
            System.out.println(contractorEdit.toString());

            //once data as been entered successfully this
            //will be printed out to the user.
            System.out.println("\nContractor details has been successfully updated!");

        }
        //if userChoice is 3.
        else if (userChoice == 3)
        {
            //conditional statement if the 'totalFeeCharge' is equal to 'amountPaid'.
            if (totalFeeCharge == amountPaid)
            {
                //message will be printed out to user if 'totalFeeCharge' is equal to 'amountPaid'.
                System.out.println("Project has been paid in full. No invoice generated!");
                //user will be asked to input the project completion date.
                System.out.println("Please add project completion date: ");

                //completion date will be stored in the
                //projectCompletion variable.
                Scanner newDate = new Scanner(System.in);
                String projectCompletion = newDate.nextLine();

                //'finalise' is to be printed out
                //for later use when we use it in the toString method below.
                String finalised = "Finalised!";

                //using the toString method created in the PoisedProgramPackage
                //to display the completion date as a well as the 'finalised' state.
                System.out.println(newProjectCaptured.toString() + "\nProject Completion Date:" + projectCompletion);
                System.out.println("\nProject Status: "+ finalised);

            }
            //conditional statement if totalFee is not equal
            //to amountPaid.
            else if (totalFeeCharge != amountPaid)
            {
                //the below message will be displayed to the user.
                System.out.println("Invoice needs to be generated with the following details below:\n");

                //user will be prompted to enter customer's name.
                //and stored in the name2 variable.
                System.out.println("Enter customer's full name: ");
                Scanner customer = new Scanner(System.in);
                String name2 = customer.nextLine();

                //to update title to 'customer'
                title = "Customer";

                //user will be prompted to enter customer contact number.
                System.out.println("Enter customer's contact number: ");
                Scanner contactNum = new Scanner(System.in);
                String number2 = contactNum.nextLine();

                //user will be prompted to enter customer email address.
                System.out.println("Enter customer's email address: ");
                Scanner contactEmail2 = new Scanner(System.in);
                String email2 = contactEmail2.nextLine();

                //user will be prompted to enter customer physical address.
                System.out.println("Enter customer's physical address: ");
                Scanner phyAddress= new Scanner(System.in);
                String address2 = phyAddress.nextLine();

                //user will be prompted to enter completion date.
                System.out.println("Enter project completion date: ");


                Scanner newDate2 = new Scanner (System.in);
                String completion2 = newDate2.nextLine();
                String finalised2 = "Finalised!";

                //the PoisedObjects class will be
                // called to display the customer details.
                PoisedObjects customer1 = new PoisedObjects(title,name2,number2,email2,address2);

                //this message will be printed to the
                //user to see the invoice below.
                System.out.println("\nPlease view your invoice below: ");

                //toString method will be called to
                //display details and amount owed.
                System.out.println(customer1.toString());
                System.out.println("Amount still owed: R"+ (totalFeeCharge - amountPaid) + "\n");

                //toString method will be called to display the completion
                //date following with the finalised state.
                System.out.println(newProjectCaptured.toString() + "\nCompletion Date: "+ completion2);
                System.out.println("Project Status: "+ finalised2);

            }

        }
        //conditional statement if userChoice is 4.
        else if (userChoice == 4)
        {
            //this message will be printed out to user.
            System.out.println("You are successfully logged out.");
        }

    }

}
