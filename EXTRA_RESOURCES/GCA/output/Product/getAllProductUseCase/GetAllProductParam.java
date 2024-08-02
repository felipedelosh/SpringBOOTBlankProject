package api.crazy.demo.domain.usecases.getAllProductUseCase;

public class GetAllProductParam {

    private GetAllProductParam(){
    }

    //This is static becos not need instance... with put static you utilized without instance.
    //Only used a method
    public static GetAllProductParam build(){
        return new GetAllProductParam();
    }
    
}
