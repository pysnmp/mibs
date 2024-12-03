#
# PySNMP MIB module IRT-COMMONVARBINDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/irt/IRT-COMMONVARBINDS-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:42:23 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
common, = mibBuilder.importSymbols("IRT-TRANSMITTER-SMI-MIB", "common")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, TimeTicks, Unsigned32, Gauge32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter32, MibIdentifier, Integer32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Unsigned32", "Gauge32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter32", "MibIdentifier", "Integer32", "iso", "ObjectIdentity")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
commonVarbinds = ModuleIdentity((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1))
commonVarbinds.setRevisions(('2007-05-04 14:00', '2006-12-20 14:00', '2006-09-21 14:00', '2006-09-19 14:00', '2006-09-07 14:00',))
if mibBuilder.loadTexts: commonVarbinds.setLastUpdated('200705041400Z')
if mibBuilder.loadTexts: commonVarbinds.setOrganization('IRT for WORKING-GROUP-TC-MIB')
objectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 1)).setObjects(("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-COMMONVARBINDS-MIB", "mibRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    objectGroup = objectGroup.setStatus('current')
eventTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
eventPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPriority.setStatus('current')
eventCounter = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCounter.setStatus('current')
mibRelease = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibRelease.setStatus('current')
commonVarbindsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 6)).setObjects(("IRT-COMMONVARBINDS-MIB", "objectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    commonVarbindsCompliance = commonVarbindsCompliance.setStatus('current')
mibBuilder.exportSymbols("IRT-COMMONVARBINDS-MIB", eventPriority=eventPriority, eventTimeStamp=eventTimeStamp, objectGroup=objectGroup, eventCounter=eventCounter, PYSNMP_MODULE_ID=commonVarbinds, mibRelease=mibRelease, commonVarbinds=commonVarbinds, commonVarbindsCompliance=commonVarbindsCompliance)
