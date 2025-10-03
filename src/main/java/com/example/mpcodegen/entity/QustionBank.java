package com.example.mpcodegen.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import java.time.LocalDate;

/**
 * <p>
 * 题库
 * </p>
 *
 * @author Yj
 * @since 2025-02-15
 */
@TableName("qustion_bank")
public class QustionBank implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;

    /**
     * 题库名称
     */
    private String name;

    /**
     * 题库介绍图
     */
    private LocalDate introduceMsg;

    /**
     * 题库介绍
     */
    private String introduce;

    /**
     * 是否vip:0.是 1.非
     */
    private Byte isVip;

    /**
     * 是否父母:0.是 1.非
     */
    private Byte isParent;

    /**
     * 是否父母:0.女 1.男 2.不分
     */
    private Byte isGender;

    /**
     * 数字人
     */
    private String digitalHuman;

    /**
     * 详细描述
     */
    private String description;

    /**
     * 序号
     */
    private Long num;

    /**
     * 是否正常:0.非正常 1.正常
     */
    private Byte status;

    /**
     * JSON视频引导
     */
    private String videoGuide;

    /**
     * 评价选项
     */
    private String config;

    /**
     * 创建人ID
     */
    private Long createUserId;

    /**
     * 更新人ID
     */
    private Long updateUserId;

    /**
     * 创建时间
     */
    private LocalDate createTime;

    /**
     * 更新时间
     */
    private LocalDate updateTime;

    /**
     * 是否删除: 0.否 1.是
     */
    private Byte isDelete;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LocalDate getIntroduceMsg() {
        return introduceMsg;
    }

    public void setIntroduceMsg(LocalDate introduceMsg) {
        this.introduceMsg = introduceMsg;
    }

    public String getIntroduce() {
        return introduce;
    }

    public void setIntroduce(String introduce) {
        this.introduce = introduce;
    }

    public Byte getIsVip() {
        return isVip;
    }

    public void setIsVip(Byte isVip) {
        this.isVip = isVip;
    }

    public Byte getIsParent() {
        return isParent;
    }

    public void setIsParent(Byte isParent) {
        this.isParent = isParent;
    }

    public Byte getIsGender() {
        return isGender;
    }

    public void setIsGender(Byte isGender) {
        this.isGender = isGender;
    }

    public String getDigitalHuman() {
        return digitalHuman;
    }

    public void setDigitalHuman(String digitalHuman) {
        this.digitalHuman = digitalHuman;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Long getNum() {
        return num;
    }

    public void setNum(Long num) {
        this.num = num;
    }

    public Byte getStatus() {
        return status;
    }

    public void setStatus(Byte status) {
        this.status = status;
    }

    public String getVideoGuide() {
        return videoGuide;
    }

    public void setVideoGuide(String videoGuide) {
        this.videoGuide = videoGuide;
    }

    public String getConfig() {
        return config;
    }

    public void setConfig(String config) {
        this.config = config;
    }

    public Long getCreateUserId() {
        return createUserId;
    }

    public void setCreateUserId(Long createUserId) {
        this.createUserId = createUserId;
    }

    public Long getUpdateUserId() {
        return updateUserId;
    }

    public void setUpdateUserId(Long updateUserId) {
        this.updateUserId = updateUserId;
    }

    public LocalDate getCreateTime() {
        return createTime;
    }

    public void setCreateTime(LocalDate createTime) {
        this.createTime = createTime;
    }

    public LocalDate getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(LocalDate updateTime) {
        this.updateTime = updateTime;
    }

    public Byte getIsDelete() {
        return isDelete;
    }

    public void setIsDelete(Byte isDelete) {
        this.isDelete = isDelete;
    }

    @Override
    public String toString() {
        return "QustionBank{" +
            "id = " + id +
            ", name = " + name +
            ", introduceMsg = " + introduceMsg +
            ", introduce = " + introduce +
            ", isVip = " + isVip +
            ", isParent = " + isParent +
            ", isGender = " + isGender +
            ", digitalHuman = " + digitalHuman +
            ", description = " + description +
            ", num = " + num +
            ", status = " + status +
            ", videoGuide = " + videoGuide +
            ", config = " + config +
            ", createUserId = " + createUserId +
            ", updateUserId = " + updateUserId +
            ", createTime = " + createTime +
            ", updateTime = " + updateTime +
            ", isDelete = " + isDelete +
        "}";
    }
}
