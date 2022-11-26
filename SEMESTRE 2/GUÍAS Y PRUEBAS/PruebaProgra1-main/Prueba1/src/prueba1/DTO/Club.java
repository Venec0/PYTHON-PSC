/**
 * @author cr.mardones
 * @fecha 14-09-2022
 */
package prueba1.DTO;

public class Club {
    private String Codigo;
    private String NombreClub;
    private String Fundador;
    private int anioFundado;
    private String Pais;
    private String Lema;
    private int ValorSuscripcion;
    private String Color1;
    private String Color2;

    public Club() {
        this.Codigo = "";
        this.NombreClub = "";
        this.Fundador = "";
        this.anioFundado = 0;
        this.Pais = "";
        this.Lema = "";
        this.ValorSuscripcion = 0;
        this.Color1 = "";
        this.Color2 = "";
    }

    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }

    public String getNombreClub() {
        return NombreClub;
    }

    public void setNombreClub(String NombreClub) {
        this.NombreClub = NombreClub;
    }

    public String getFundador() {
        return Fundador;
    }

    public void setFundador(String Fundador) {
        this.Fundador = Fundador;
    }

    public int getAnioFundado() {
        return anioFundado;
    }

    public void setAnioFundado(int anioFundado) {
        this.anioFundado = anioFundado;
    }

    public String getPais() {
        return Pais;
    }

    public void setPais(String Pais) {
        this.Pais = Pais;
    }

    public String getLema() {
        return Lema;
    }

    public void setLema(String Lema) {
        this.Lema = Lema;
    }

    public int getValorSuscripcion() {
        return ValorSuscripcion;
    }

    public void setValorSuscripcion(int ValorSuscripcion) {
        this.ValorSuscripcion = ValorSuscripcion;
    }

    public String getColor1() {
        return Color1;
    }

    public void setColor1(String Color1) {
        this.Color1 = Color1;
    }

    public String getColor2() {
        return Color2;
    }

    public void setColor2(String Color2) {
        this.Color2 = Color2;
    }
}
