/**
 * @author cr.mardones
 * @fecha 14-09-2022
 */
package prueba1.DTO;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import prueba1.Metodos.Metodo;
public class Usuario {
    private int ID;
    private String PrimerNombre;
    private String SegundoNombre;
    private String ApellidoPaterno;
    private String ApellidoMaterno;
    private int Rut;
    private String Dv;
    private String FechaNacimiento;
    private int Telefono;
    private String NombreUsuario;
    private String Email;
    private String Password;   

    public Usuario() {
        this.ID = 1000;
        this.PrimerNombre = "";
        this.SegundoNombre = "";
        this.ApellidoPaterno = "";
        this.ApellidoMaterno = "";
        this.Rut = 0;
        this.Dv = "";
        this.FechaNacimiento = "";
        this.Telefono = 0;
        this.NombreUsuario = "";
        this.Email = "";
        this.Password = "";
    }
    
    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        
        this.ID = ID;
    }

    public String getPrimerNombre() {
        return PrimerNombre;
    }

    public void setPrimerNombre(String PrimerNombre) {
        if(PrimerNombre.length()>4){
            this.PrimerNombre = PrimerNombre;
        }
        else{
            System.out.println("Nombre no valida debe tener al menos 4 caracteres");
        }
            
    }

    public String getSegundoNombre() {
        
        return SegundoNombre;
    }

    public void setSegundoNombre(String SegundoNombre) {
        this.SegundoNombre = SegundoNombre;
    }

    public String getApellidoPaterno() {
        return ApellidoPaterno;
    }

    public void setApellidoPaterno(String ApellidoPaterno) {
        this.ApellidoPaterno = ApellidoPaterno;
    }

    public String getApellidoMaterno() {
        return ApellidoMaterno;
    }

    public void setApellidoMaterno(String ApellidoMaterno) {
        if(PrimerNombre.length()>4){
            this.ApellidoMaterno = ApellidoMaterno;
        }
        else{
            System.out.println("Apellido no validado debe tener al menos 4 caracteres");
        }
        
    }

    public int getRut() {
        return Rut;
    }

    public void setRut(int Rut) {
         this.Rut = Rut;
    }

    public String getDv() {
        return Dv;
    }

    public void setDv(String Dv) {
        this.Dv = Dv;
    }

    public String getFechaNacimiento() {
        
        return Edad();
    }

    public void setFechaNacimiento(String FechaNacimiento) {
        this.FechaNacimiento = FechaNacimiento;
    }

    public int getTelefono() {
        return Telefono;
    }

    public void setTelefono(int Telefono) {
        if(String.valueOf(Telefono).length()>=8 && String.valueOf(Telefono).contains("56")){
            this.Telefono = Telefono;
        }
        else{
            System.out.println("Telefono debe tener 56 y mas de 8 caracteres");
        }
        
    }

    public String getNombreUsuario() {
        
        return NombreUsuario;
    }

    public void setNombreUsuario(String NombreUsuario) {
        if(NombreUsuario.length()>=4){
            this.NombreUsuario = NombreUsuario;
        }
        else{
            System.out.println("nombre no valido");
        }
    }

    public String getEmail() {
        
        return Email;
    }

    public void setEmail(String Email) {
        if(Email.contains("@") && (Email.contains(".com") || Email.contains(".cl")) && Email.length()>4){
            this.Email = Email;
        }
        else{
            System.out.println("El correo debe contener un @ y el .com ademas, debe tener al menos 4 caracteres");
        }
        
    }

    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        Metodo met = new Metodo();
        if(met.ValidaPassword(Password)){
            this.Password = Password;
            System.out.println("Password Ingresada correctamente");
        }
        else{
            System.out.println("Password ingresada no valida");
        }       
    }
    public String Edad(){
        LocalDate FechaActual = LocalDate.now();
        DateTimeFormatter Formato = DateTimeFormatter.ofPattern("yyyy/MM/dd");
        LocalDate FechaNacFormato = LocalDate.parse(this.FechaNacimiento, Formato);
        Period Edad = Period.between(FechaNacFormato, FechaActual);
        return "La edad es: "+Edad.getYears()+" anios ";
    }
    
    
    
}
