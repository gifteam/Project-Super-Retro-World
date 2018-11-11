using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VHSClass : MonoBehaviour {

    //Class variable
    private GO m_filter;

	// Use this for initialization
	void Start () {
        GameObject l_filter_GO = GameObject.FindWithTag("PowerUp");
        m_filter = new GO(l_filter_GO);
        m_filter.getGO().SetActive(false);
    }
	
	// Update is called once per frame
	void Update () {
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.CompareTag("Player"))
        {
            m_filter.getGO().SetActive(true);
            Destroy(gameObject);
        }
    }
}
