//WANING: this code is autogenerated with GCA by FelipedelosH
package api.crazy.demo.domain.usecases.getAllTestOneVarIntUseCase;

import java.util.List;
import java.util.ArrayList;
import org.springframework.stereotype.Component;

import api.crazy.demo.domain.entities.TestOneVarInt;
import api.crazy.demo.infraestructure.DAO.TestOneVarIntDAO.TestOneVarIntEntity;
import api.crazy.demo.infraestructure.DAO.TestOneVarIntDAO.TestOneVarIntService;
//Convert database info in Java Class
import api.crazy.demo.infraestructure.mappers.TestOneVarIntMapper;

@Component //This decorator permit injection
public class GetAllTestOneVarIntUseCaseImpl extends GetAllTestOneVarIntUseCase {

    private final TestOneVarIntService testonevarintservice;

    public GetAllTestOneVarIntUseCaseImpl(TestOneVarIntService testonevarintservice){
        this.testonevarintservice = testonevarintservice;
    }

    @Override
    public List<TestOneVarInt> call(GetAllTestOneVarIntUseCaseParam param) {

        List<TestOneVarInt> x = new ArrayList<>();
        List<TestOneVarIntEntity> y = testonevarintservice.getAll();

        for (int i = 0; i < y.size(); i++) {
            x.add(TestOneVarIntMapper.toDomain(y.get(i)));
        }

        return x;
    }

}
