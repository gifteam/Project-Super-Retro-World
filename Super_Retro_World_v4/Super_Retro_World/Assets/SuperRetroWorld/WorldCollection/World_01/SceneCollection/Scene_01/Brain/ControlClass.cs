using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Control
{
    public List<float> m_keys;
    public bool m_left;
    public bool m_right;
    public bool m_up;

    public Control()
    {
        m_keys = new List<float>();
        m_keys.Add(0f);
        m_keys.Add(0f);
        m_keys.Add(0f);
        m_left = false;
        m_right = false;
        m_up = false;
    }

    public void setKeys()
    {
        resetKeys();
        if (m_keys[0] > 0) { m_left  = true; }
        if (m_keys[1] > 0) { m_right = true; }
        if (m_keys[2] > 0) { m_up    = true; }

        for (int i_keyIndex = 0; i_keyIndex < m_keys.Count; i_keyIndex++)
        {
            m_keys[i_keyIndex] = 0.0f;
        }
    }

    public void resetKeys()
    {
        m_left = false;
        m_right = false;
        m_up = false;
    }
}
