package com.HTM.service;
 
import java.util.List;
 
import com.HTM.vo.MovieVO;
 
public interface MovieService {
    
    public List<MovieVO> selectMovie() throws Exception;
}