package api.crazy.demo.domain.usecases.getAllOrderUseCase;

public class GetAllOrderParam {

    private GetAllOrderParam(){
    }

    //This is static becos not need instance... with put static you utilized without instance.
    //Only used a method
    public static GetAllOrderParam build(){
        return new GetAllOrderParam();
    }
    
}
