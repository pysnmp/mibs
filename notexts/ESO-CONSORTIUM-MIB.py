#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:18:14 2024
# On host fv-az530-683 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Unsigned32, NotificationType, ModuleIdentity, Bits, Integer32, Gauge32, IpAddress, Counter32, iso, MibIdentifier, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Unsigned32", "NotificationType", "ModuleIdentity", "Bits", "Integer32", "Gauge32", "IpAddress", "Counter32", "iso", "MibIdentifier", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter64")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
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
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", esoConsortiumMIB=esoConsortiumMIB, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, PYSNMP_MODULE_ID=esoConsortiumMIB, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, usm3DESPrivProtocol=usm3DESPrivProtocol, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol)
