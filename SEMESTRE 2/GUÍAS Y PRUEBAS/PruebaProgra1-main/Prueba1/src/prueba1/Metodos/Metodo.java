/**
 * @author cr.mardones
 * @fecha 14-09-2022
 */
package prueba1.Metodos;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.Date;
public class Metodo {
    
    public static boolean ValidaPassword(String pass){
        boolean validaMayu = false;
        boolean validaNum = false;
        if(pass.length()>5){
            for(int x=0;x<pass.length();x++){
                if(!Character.isUpperCase(pass.charAt(x))){
                    validaMayu = true;
                }            
                else if(!Character.isDigit(pass.charAt(x))){
                    validaNum = true;
                }
            }
            if(validaMayu==true && validaNum==true){
                return true;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }       
    }
    
    public static boolean ValidarDv(String rut, String dv){
        boolean Validacion=false;
        char Dv;
        if(rut.length()==8 || rut.length()==7){
            if(rut.contains(".")){
                rut = rut.replace(".","");
            }
            if(rut.contains("-")){
                rut = rut.replace("-", "");                
            }
            int rutAux = Integer.parseInt(rut);
            Dv = dv.charAt(0);
            int m = 0, s = 1;
            for (; rutAux != 0; rutAux /= 10) {
                s = (s + rutAux % 10 * (9 - m++ % 6)) % 11;
            }
            if (Dv == (char) (s != 0 ? s + 47 : 75)) {
                Validacion = true;
            }   
        }
        return Validacion;
    }
    
    
}