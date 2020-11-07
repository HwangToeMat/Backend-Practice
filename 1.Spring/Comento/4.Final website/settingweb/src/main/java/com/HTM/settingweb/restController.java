package com.HTM.settingweb;
 
import java.util.List;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.slf4j.LoggerFactory;
import org.slf4j.Logger;
import javax.inject.Inject;
import com.HTM.service.*;
import com.HTM.vo.*;

@RestController
public class restController {
    
    private static final Logger logger = LoggerFactory.getLogger(restController.class);
    
    @Inject
    private MovieService service;
    
    /**
     * Simply selects the home view to render by returning its name.
     */
    @RequestMapping(value = "/restex")
    public List<MovieVO> movieList(Model model) throws Exception{
 
        logger.info("home");
        
        List<MovieVO> movieList = service.selectMovie();
        
        model.addAttribute("movieList", movieList);
 
        return movieList;
    }
    @RequestMapping(value = "/mean")
    
    public List<MovieVO> mean_list(Model model) throws Exception{
 
        logger.info("home");
        
        List<MovieVO> mean_list = service.selectMovie();
        
        model.addAttribute("mean_list", mean_list);
 
        return mean_list;
    }
    
}
