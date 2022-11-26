/**
 * @author cr.mardones
 * @fecha 14-09-2022
 */
package prueba1;
import java.util.Scanner;
import prueba1.DTO.Usuario;
import prueba1.DTO.Club;
import prueba1.DTO.Suscripcion;
import prueba1.Metodos.Metodo;
public class principal {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Usuario usu = new Usuario();  
        int ID=1000;
        //creamos usuario 1    
        usu.setID(ID);
        usu.setPrimerNombre("Cristian");
        usu.setSegundoNombre("Eduardo");
        usu.setApellidoPaterno("Mardones");
        usu.setApellidoMaterno("Perez");        
        usu.setTelefono(56520050);             
        usu.setNombreUsuario("dcog");
        usu.setPassword("Qwerty1");
        System.out.println("ingrese su rut sin sigito verificador ni punto ni guion");
        int rut = sc.nextInt();
        System.out.println("ingrese su digito verificador");
        String dv = sc.next();
        boolean valida = Metodo.ValidarDv(String.valueOf(rut),dv);
        if(valida==true){
            usu.setRut(rut);
            usu.setDv(dv);
        }
        else{
            System.out.println("El rut ingresado no es valido");
        }        
        usu.setFechaNacimiento("1994/05/22");  
        
        //creamos primer club
        String Deporte = "Handball";
        Club cl = new Club();
        int correlativo=10;
        cl.setNombreClub("Arsenal de Coquimbo");
        cl.setCodigo(cl.getNombreClub().substring(0,2).toUpperCase()+Deporte.substring(0,1)+correlativo);
        cl.setFundador("Cristian Mardones");
        cl.setAnioFundado(2000);
        cl.setPais("Chile");
        cl.setLema("Canones a los puertos");
        cl.setValorSuscripcion(10050);
        cl.setColor1("Amarillo");
        cl.setColor2("Rojo");    
        correlativo = correlativo+10;
        
        
        
        
        
        
        
        
        
        
    }
    
}
