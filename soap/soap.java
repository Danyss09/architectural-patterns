import javax.jws.WebService;
import javax.jws.WebMethod;

@WebService
public class HelloWorld {
    @WebMethod
    public String sayHello() {
        return "Hello World, my name is Daniela Cáceres!";
    }
}
