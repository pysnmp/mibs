#
# PySNMP MIB module A10-AX-SCALEOUT-TRAPS-V1 (http://snmplabs.com/pysmi)
# ASN.1 source A10-AX-SCALEOUT-TRAPS-V1
# Source digest sha256:1ec18913e5c03b74a06876de006518131914e52545a44b6d0b598368b197084f
# Produced by pysmi-2.3.0
#
axLogging, axNotification = mibBuilder.importSymbols("A10-AX-MIB", "axLogging", "axNotification")
axNotificationMsg, axNotificationScaleOutDeviceId, axNotificationScaleOutNumberOfDevice, axNotificationScaleOutStatus, axNotificationScaleOutTrafficMapType, axNotifications = mibBuilder.importSymbols("A10-AX-NOTIF-OBJ", "axNotificationMsg", "axNotificationScaleOutDeviceId", "axNotificationScaleOutNumberOfDevice", "axNotificationScaleOutStatus", "axNotificationScaleOutTrafficMapType", "axNotifications")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
axScaleoutNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7))
axScaleoutVserverTrafficMap = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,1)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
axScaleoutLocalNodeDisabled = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,2)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
axScaleoutServiceMaster = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,3)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutDeviceId"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus"))
axScaleoutSingleNodeStatus = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,4)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus"))
axScaleoutElection = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,5)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutNumberOfDevice"))
axScaleoutMasterNodeCallingReelection = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,6)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
axScaleoutNodeStatus = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,7)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutDeviceId"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutStatus"))
axScaleoutTrafficMapUpdate = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,8)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"), ("A10-AX-NOTIF-OBJ", "axNotificationScaleOutTrafficMapType"))
axScaleoutTrafficMapDistribution = NotificationType((1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 7) + (0,9)).setObjects(("A10-AX-NOTIF-OBJ", "axNotificationMsg"))
mibBuilder.exportSymbols("A10-AX-SCALEOUT-TRAPS-V1", axScaleoutElection=axScaleoutElection, axScaleoutLocalNodeDisabled=axScaleoutLocalNodeDisabled, axScaleoutMasterNodeCallingReelection=axScaleoutMasterNodeCallingReelection, axScaleoutNodeStatus=axScaleoutNodeStatus, axScaleoutNotifications=axScaleoutNotifications, axScaleoutServiceMaster=axScaleoutServiceMaster, axScaleoutSingleNodeStatus=axScaleoutSingleNodeStatus, axScaleoutTrafficMapDistribution=axScaleoutTrafficMapDistribution, axScaleoutTrafficMapUpdate=axScaleoutTrafficMapUpdate, axScaleoutVserverTrafficMap=axScaleoutVserverTrafficMap)
