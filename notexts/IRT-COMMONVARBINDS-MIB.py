#
# PySNMP MIB module IRT-COMMONVARBINDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-COMMONVARBINDS-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:46:04 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
common, = mibBuilder.importSymbols("IRT-TRANSMITTER-SMI-MIB", "common")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, Unsigned32, iso, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Integer32, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Unsigned32", "iso", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
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
mibBuilder.exportSymbols("IRT-COMMONVARBINDS-MIB", mibRelease=mibRelease, eventTimeStamp=eventTimeStamp, eventPriority=eventPriority, objectGroup=objectGroup, PYSNMP_MODULE_ID=commonVarbinds, eventCounter=eventCounter, commonVarbinds=commonVarbinds, commonVarbindsCompliance=commonVarbindsCompliance)
