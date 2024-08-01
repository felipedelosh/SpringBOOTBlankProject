package api.crazy.demo;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

@Configuration
@ComponentScan(
basePackages = "api.crazy.demo.domain.usecases",
includeFilters = {
    @ComponentScan.Filter(type = FilterType.REGEX, pattern = "^.+UseCase$"),
    @ComponentScan.Filter(type = FilterType.REGEX, pattern = "^.+UseCaseImpl$"),
},
useDefaultFilters = false)
public class ConfigurationAPP {
  
}
