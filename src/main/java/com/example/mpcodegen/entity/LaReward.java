package com.example.mpcodegen.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * <p>
 * 奖品表
 * </p>
 *
 * @author Yj
 * @since 2025-02-12
 */
@TableName("la_reward")
public class LaReward implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;

    /**
     * 奖品名称
     */
    private String name;

    /**
     * 活动图片
     */
    private String photo;

    /**
     * 类型:1-勋章,2 - 奖品,3-会员
     */
    private Byte type;

    /**
     * 是否限制人数:0.限制,1.不限制
     */
    private Byte isLimit;

    /**
     * 数量
     */
    private Byte num;

    /**
     * 状态：1.启动 2.禁用
     */
    private Byte status;

    /**
     * 活动id
     */
    private Long activityId;

    /**
     * 创建时间
     */
    private LocalDateTime createTime;

    /**
     * 更新时间
     */
    private LocalDateTime updateTime;

    /**
     * 创建人ID
     */
    private Long createUserId;

    /**
     * 更新人ID
     */
    private Long updateUserId;

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

    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }

    public Byte getType() {
        return type;
    }

    public void setType(Byte type) {
        this.type = type;
    }

    public Byte getIsLimit() {
        return isLimit;
    }

    public void setIsLimit(Byte isLimit) {
        this.isLimit = isLimit;
    }

    public Byte getNum() {
        return num;
    }

    public void setNum(Byte num) {
        this.num = num;
    }

    public Byte getStatus() {
        return status;
    }

    public void setStatus(Byte status) {
        this.status = status;
    }

    public Long getActivityId() {
        return activityId;
    }

    public void setActivityId(Long activityId) {
        this.activityId = activityId;
    }

    public LocalDateTime getCreateTime() {
        return createTime;
    }

    public void setCreateTime(LocalDateTime createTime) {
        this.createTime = createTime;
    }

    public LocalDateTime getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(LocalDateTime updateTime) {
        this.updateTime = updateTime;
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

    public Byte getIsDelete() {
        return isDelete;
    }

    public void setIsDelete(Byte isDelete) {
        this.isDelete = isDelete;
    }

    @Override
    public String toString() {
        return "LaReward{" +
            "id = " + id +
            ", name = " + name +
            ", photo = " + photo +
            ", type = " + type +
            ", isLimit = " + isLimit +
            ", num = " + num +
            ", status = " + status +
            ", activityId = " + activityId +
            ", createTime = " + createTime +
            ", updateTime = " + updateTime +
            ", createUserId = " + createUserId +
            ", updateUserId = " + updateUserId +
            ", isDelete = " + isDelete +
        "}";
    }
}
