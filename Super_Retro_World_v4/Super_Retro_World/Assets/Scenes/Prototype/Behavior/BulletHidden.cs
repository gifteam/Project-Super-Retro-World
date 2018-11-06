using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletHidden : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        Vector2 pos = transform.parent.transform.position;
        gameObject.transform.position = pos;
    }
}
