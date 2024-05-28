#
# PySNMP MIB module IRT-COMMONVARBINDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-COMMONVARBINDS-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:13:51 2024
# On host fv-az1789-536 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
common, = mibBuilder.importSymbols("IRT-TRANSMITTER-SMI-MIB", "common")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Integer32, Unsigned32, Counter64, TimeTicks, Counter32, ObjectIdentity, Gauge32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Unsigned32", "Counter64", "TimeTicks", "Counter32", "ObjectIdentity", "Gauge32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Bits")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
commonVarbinds = ModuleIdentity((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1))
commonVarbinds.setRevisions(('2007-05-04 14:00', '2006-12-20 14:00', '2006-09-21 14:00', '2006-09-19 14:00', '2006-09-07 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: commonVarbinds.setRevisionsDescriptions(('change MODULE-COMPLIANCE', 'corrections', 'Adding Compliance Statement', 'Channing commonVarbins form 7.2 to 7.1', 'Relocation of the TC-MIB from the standard OID area at IEC into the private OID area of the IRT',))
if mibBuilder.loadTexts: commonVarbinds.setLastUpdated('200705041400Z')
if mibBuilder.loadTexts: commonVarbinds.setOrganization('IRT for WORKING-GROUP-TC-MIB')
if mibBuilder.loadTexts: commonVarbinds.setContactInfo('Contact-info:\n\t\t\t\t\n\t\t\t\tAndreas Metz\n\t\t\t\t\n\t\t\t\tInstitut fuer Rundfunktechnik GmbH\n\t\t\t\tBroadcast Networks and Servers (SN)\n\t\t\t\t\n\t\t\t\tFloriansmuehlstr.60\n\t\t\t\t80939 Munich\n\t\t\t\tGermany\n\t\t\t\t\n\t\t\t\tPhone: +49 89 32399 325\n\t\t\t\tFax: +49 89 32399 354\n\t\t\t\t')
if mibBuilder.loadTexts: commonVarbinds.setDescription('Description:\n\t\t\t\t   \n\t\t\t\tCommon values')
objectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 1)).setObjects(("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-COMMONVARBINDS-MIB", "mibRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    objectGroup = objectGroup.setStatus('current')
if mibBuilder.loadTexts: objectGroup.setDescription('Description. Common objects')
eventTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
if mibBuilder.loadTexts: eventTimeStamp.setDescription('Description.Event timestamp in UTC')
eventPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPriority.setStatus('current')
if mibBuilder.loadTexts: eventPriority.setDescription('Description.Event priority level')
eventCounter = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCounter.setStatus('current')
if mibBuilder.loadTexts: eventCounter.setDescription('Description.Event counter')
mibRelease = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibRelease.setStatus('current')
if mibBuilder.loadTexts: mibRelease.setDescription('Description.The current MIB version')
commonVarbindsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7, 1, 6)).setObjects(("IRT-COMMONVARBINDS-MIB", "objectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    commonVarbindsCompliance = commonVarbindsCompliance.setStatus('current')
if mibBuilder.loadTexts: commonVarbindsCompliance.setDescription('Compliance Statement')
mibBuilder.exportSymbols("IRT-COMMONVARBINDS-MIB", mibRelease=mibRelease, commonVarbindsCompliance=commonVarbindsCompliance, eventPriority=eventPriority, objectGroup=objectGroup, commonVarbinds=commonVarbinds, eventCounter=eventCounter, eventTimeStamp=eventTimeStamp, PYSNMP_MODULE_ID=commonVarbinds)
