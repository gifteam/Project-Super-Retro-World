using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TrackerClass : MonoBehaviour {

    public GO m_target;
    public GO m_go;
    public float m_trackerSpeed;
    public int m_hitCount;
    public int m_recovery;

    // Use this for initialization
    void Start () {
        m_trackerSpeed = 0.04f;
        m_recovery = 120;
        m_hitCount = 3;
        m_go = new GO(gameObject);
    }
	
	// Update is called once per frame
	void Update () {

        if (m_target != null)
        {
            if (m_recovery > 0)
            {
                m_recovery--;
            }

            Vector2 l_pos = m_go.posCen();
            Vector2 l_targetPos = m_target.posCen();

            float l_deltaX = l_pos.x - l_targetPos.x;
            float l_deltaY = l_pos.y - l_targetPos.y;

            if (l_deltaX > 0)
            {
                l_pos.x -= m_trackerSpeed;
            }
            else
            {
                l_pos.x += m_trackerSpeed;
            }

            if (l_deltaY > 0)
            {
                l_pos.y -= m_trackerSpeed;
            }
            else
            {
                l_pos.y += m_trackerSpeed;
            }

            m_go.setPos(l_pos);
        }
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (m_target != null)
        {
            if (other.gameObject.GetInstanceID() == m_target.getGO().GetInstanceID() && m_recovery == 0)
            {
                if (m_hitCount > 0)
                {
                    m_hitCount--;
                    m_recovery = 100;
                }
                else
                {
                    Destroy(other.gameObject);
                    Destroy(m_go.getGO());
                }
            }
        }
    }

    private void OnTriggerStay2D(Collider2D other)
    {
        if (m_target != null)
        {
            if (other.gameObject.GetInstanceID() == m_target.getGO().GetInstanceID() && m_recovery == 0)
            {
                if (m_hitCount > 0)
                {
                    m_hitCount--;
                    m_recovery = 100;
                }
                else
                {
                    Destroy(other.gameObject);
                    Destroy(m_go.getGO());
                }
            }
        }
    }
}
