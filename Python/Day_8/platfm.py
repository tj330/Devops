import platform as p

m_uname = p.uname()

m_os = m_uname.system

m_release = m_uname.release

m_version = m_uname.version

m_type = m_uname.machine

m_name = m_uname.node

m_arch = p.architecture()

try:
    with open("system_info.txt", "w") as f:
        info = f"""Platform information:\n
                    OS name: {m_os}\n
                    release: {m_release}\n 
                    version: {m_version}\n 
                    machine type: {m_type}\n 
                    hostname: {m_name}\n 
                    architecture: {m_arch}\n 
            """
        f.write(info)
        print("Platform information successfully saved in system_info.txt")

except Exception as e:
    print(f"Error occured: {e}")

