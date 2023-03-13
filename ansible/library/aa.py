--- helm_toolbox.py	(original)
+++ helm_toolbox.py	(refactored)
@@ -19,7 +19,7 @@
 
 from ansible.module_utils.basic import AnsibleModule
 
-print "asdasdsa"
+print("asdasdsa")
 DOCUMENTATION = '''
 ---
 module: helm_toolbox
@@ -105,7 +105,7 @@
                 chart_extra_vars = self.params.get('chart_extra_vars')
                 if isinstance(chart_extra_vars, dict):
                     chart_extra_cmd = ' '.join('--set {}={}'.format(key, value)  # noqa
-                                      for key, value in chart_extra_vars.items() if value)  # noqa
+                                      for key, value in list(chart_extra_vars.items()) if value)  # noqa
 
                     cmd.append(chart_extra_cmd)
 
