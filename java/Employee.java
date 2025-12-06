//Develop the Employee class and suitable main method for demonstration. 

public class Employee {

    private final int id;
    private final String name;
    private double salary;

    public Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    public void raiseSalary(double percent) {
        if (percent > 0) {
            double raiseAmount = salary * (percent / 100);
            salary += raiseAmount;
            System.out.println(name + "'s salary raised by " + percent + "%. New salary: $" + salary);
        } else {

            System.out.println("Invalid percentage. Salary remains unchanged.");
        }
    }

    @Override
    public String toString() {
        return "Employee ID: " + id + ", Name: " + name + ", Salary: $" + salary;
    }

    public static void main(String[] args) {
        // Creating an Employee object 
        Employee employee1 = new Employee(1, "John Doe", 50000.0);
        Employee employee2 = new Employee(2, "Sachin Kumar", 45000.0);

        // Displaying employee details 
        System.out.println("Initial Employee Details of employee1:");
        System.out.println(employee1);
// Raising salary by 10% 
        employee1.raiseSalary(10);

// Displaying updated employee details 
        System.out.println("\nEmployee Details after Salary Raise:");
        System.out.println(employee1);
        System.out.println();

        System.out.println("Initial Employee Details of employee2:");
        System.out.println(employee2);
// Raising salary by 15% 
        employee2.raiseSalary(15);

// Displaying updated employee details 
        System.out.println("\nEmployee Details after Salary Raise:");
        System.out.println(employee2);

    }
}
