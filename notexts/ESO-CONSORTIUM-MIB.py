#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:23:16 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, snmpModules, TimeTicks, NotificationType, enterprises, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, MibIdentifier, Counter64, ObjectIdentity, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "snmpModules", "TimeTicks", "NotificationType", "enterprises", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "MibIdentifier", "Counter64", "ObjectIdentity", "Bits", "Gauge32")
TextualConvention, AutonomousType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "DisplayString")
esoConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
esoConsortiumMIB.setRevisions(('2004-06-23 00:00', '2003-02-03 00:00', '2003-02-03 00:00',))
if mibBuilder.loadTexts: esoConsortiumMIB.setLastUpdated('200406230000Z')
if mibBuilder.loadTexts: esoConsortiumMIB.setOrganization('ESO (Extended Security Options) Consortium')
esoConsortiumMIBObjectIdentities = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
usmAESCfb128PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 2))
if mibBuilder.loadTexts: usmAESCfb128PrivProtocol.setStatus('deprecated')
usmAESCfb192PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 3))
if mibBuilder.loadTexts: usmAESCfb192PrivProtocol.setStatus('current')
usmAESCfb256PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 4))
if mibBuilder.loadTexts: usmAESCfb256PrivProtocol.setStatus('current')
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, usm3DESPrivProtocol=usm3DESPrivProtocol, esoConsortiumMIB=esoConsortiumMIB, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, PYSNMP_MODULE_ID=esoConsortiumMIB)
