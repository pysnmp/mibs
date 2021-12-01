#
# PySNMP MIB module IRT-COMMONVARBINDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-COMMONVARBINDS-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 16:35:59 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
common, = mibBuilder.importSymbols("IRT-TRANSMITTER-SMI-MIB", "common")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Integer32, MibIdentifier, iso, NotificationType, Bits, Counter32, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Integer32", "MibIdentifier", "iso", "NotificationType", "Bits", "Counter32", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("IRT-COMMONVARBINDS-MIB", eventCounter=eventCounter, eventTimeStamp=eventTimeStamp, eventPriority=eventPriority, mibRelease=mibRelease, PYSNMP_MODULE_ID=commonVarbinds, objectGroup=objectGroup, commonVarbinds=commonVarbinds, commonVarbindsCompliance=commonVarbindsCompliance)
