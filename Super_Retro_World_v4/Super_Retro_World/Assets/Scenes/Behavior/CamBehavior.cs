using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CamBehavior : MonoBehaviour {

    public int xMin;
    public int xMax;
    public int yMin;
    public int yMax;

    public GameObject target;

	// Use this for initialization
	void Start () {

        //looking for one specific target to center the camera with
        target = getNewTarget("Player");

        xMin = -100;
        xMax = 100;
        yMin = 3;
        yMax = 10;
}
	
	// Update is called once per frame
	void LateUpdate () {

        float x = Mathf.Clamp(getTargetX(), xMin, xMax);
        float y = Mathf.Clamp(getTargetY(), yMin, yMax);
        float z = gameObject.transform.position.z;

        gameObject.transform.position = new Vector3(x, y, z);
    }


    GameObject getNewTarget(string tag)
    {
        return GameObject.FindGameObjectWithTag(tag);
    }

    float getTargetX()
    {
        return target.transform.position.x;
    }

    float getTargetY()
    {
        return target.transform.position.y;
    }
}
