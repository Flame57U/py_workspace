package com.example.mpcodegen.service.impl;

import com.example.mpcodegen.entity.Employees;
import com.example.mpcodegen.mapper.EmployeesMapper;
import com.example.mpcodegen.service.IEmployeesService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author Yj
 * @since 2025-02-12
 */
@Service
public class EmployeesServiceImpl extends ServiceImpl<EmployeesMapper, Employees> implements IEmployeesService {

}
