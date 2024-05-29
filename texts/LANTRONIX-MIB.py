#
# PySNMP MIB module LANTRONIX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lantronix/LANTRONIX-MIB.mib
# Produced by pysmi-1.1.12 at Wed May 29 08:12:46 2024
# On host fv-az698-992 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Counter64, Counter32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, iso, ModuleIdentity, Gauge32, TimeTicks, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Counter64", "Counter32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "iso", "ModuleIdentity", "Gauge32", "TimeTicks", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lantronix = ModuleIdentity((1, 3, 6, 1, 4, 1, 244))
lantronix.setRevisions(('2007-03-01 00:00', '2006-11-10 00:00', '2004-12-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lantronix.setRevisionsDescriptions(('Added legacy products.', 'Added sls product.', 'The initial version of the MIB module.',))
if mibBuilder.loadTexts: lantronix.setLastUpdated('200703010000Z')
if mibBuilder.loadTexts: lantronix.setOrganization('Lantronix, Inc.')
if mibBuilder.loadTexts: lantronix.setContactInfo('Lantronix Technical Support\n                  15353 Barranca Parkway\n                  Irvine, CA 92618 USA\n                  +1 800 422-7044\n                  snmp@lantronix.com')
if mibBuilder.loadTexts: lantronix.setDescription('The structure of Management Information for the Lantronix enterprise')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1))
slc = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 1))
slk = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 8))
slp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9))
slm = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 10))
sls = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 11))
ltxlna = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 10))
ltxlrp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 11))
ltxlsw = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 12))
mibBuilder.exportSymbols("LANTRONIX-MIB", ltxlsw=ltxlsw, slc=slc, slk=slk, slm=slm, products=products, PYSNMP_MODULE_ID=lantronix, slp=slp, lantronix=lantronix, sls=sls, ltxlrp=ltxlrp, ltxlna=ltxlna)
