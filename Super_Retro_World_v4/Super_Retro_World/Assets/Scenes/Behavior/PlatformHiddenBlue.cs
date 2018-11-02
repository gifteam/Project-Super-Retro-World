using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlatformHiddenBlue : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        Vector2 pos = transform.parent.transform.position;
        pos.x += 0.22f;
        gameObject.transform.position = pos;
    }
}
