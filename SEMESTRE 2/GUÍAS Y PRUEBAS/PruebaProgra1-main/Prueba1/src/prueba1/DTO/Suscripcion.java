/**
 * @author cr.mardones
 * @fecha 14-09-2022
 */
package prueba1.DTO;
import java.util.Date;
public class Suscripcion {
    private Date FechaInicio;
    private int ValorSuscripcion;
    private int Abono;
    private String Club;
    private String Usuario;

    public Suscripcion() {
        this.FechaInicio = new Date();
        this.ValorSuscripcion = 0;
        this.Abono = 0;
        this.Club = "";
        this.Usuario = "";
    }

    public Date getFechaInicio() {
        return FechaInicio;
    }

    public void setFechaInicio(Date FechaInicio) {
        this.FechaInicio = FechaInicio;
    }

    public int getValorSuscripcion() {
        return ValorSuscripcion;
    }

    public void setValorSuscripcion(int ValorSuscripcion) {
        this.ValorSuscripcion = ValorSuscripcion;
    }

    public int getAbono() {
        return Abono;
    }

    public void setAbono(int Abono) {
        this.Abono = Abono;
    }

    public String getClub() {
        return Club;
    }

    public void setClub(String Club) {
        this.Club = Club;
    }

    public String getUsuario() {
        return Usuario;
    }

    public void setUsuario(String Usuario) {
        this.Usuario = Usuario;
    }
    
    
}
