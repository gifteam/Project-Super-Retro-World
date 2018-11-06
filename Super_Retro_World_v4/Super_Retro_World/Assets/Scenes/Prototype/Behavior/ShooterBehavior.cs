using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShooterBehavior : MonoBehaviour {

    public GameObject target;
    public GameObject bullet;
    public float rangeX;
    public float rangeXsq;
    public Vector2 pos;
    public Vector2 targetPos;
    public float distToTarget;

    public bool hasShoot;
    public ulong reloadCooldownMax;
    public ulong reloadCooldown;

    // Use this for initialization
    void Start () {
        target = getNewGameObject("Player");
        bullet = getNewGameObject("Bullet");
        rangeX = 10;
        rangeXsq = rangeX * rangeX;
        distToTarget = -1;
        hasShoot = false;
        reloadCooldownMax = 200;
        reloadCooldown = reloadCooldownMax;
    }
	
	// Update is called once per frame
	void Update () {

        //is target in global range
        pos = getPos();
        targetPos = getTargetPos();

        if (!hasShoot)
        {
            if (targetIsInRangeX())
            {
                bullet.GetComponent<BulletBehavior>().setTarget(target);
                bullet.GetComponent<BulletBehavior>().load(pos);
                bullet.GetComponent<BulletBehavior>().shoot();
                hasShoot = true;
            }
        }
        else
        {
            reloadCooldown--;
            if (reloadCooldown <= 0)
            {
                reloadCooldown = reloadCooldownMax;
                hasShoot = false;
            }
        }

	}

    bool targetIsInRangeX()
    {
        float x1 = pos.x;
        float x2 = targetPos.x;

        float y1 = pos.y;
        float y2 = targetPos.y;

        float distMin = rangeXsq;
        distToTarget = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);

        if (distToTarget <= distMin)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    GameObject getNewGameObject(string tag)
    {
        return GameObject.FindGameObjectWithTag(tag);
    }

    Vector2 getPos()
    {
        return transform.position;
    }

    Vector2 getTargetPos()
    {
        return target.transform.position;
    }
}
